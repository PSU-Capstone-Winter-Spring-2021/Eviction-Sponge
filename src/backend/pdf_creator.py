from dataclasses import dataclass
import pdfrw
import datetime
from form_filling import FormData, PDF_form_template
from src.backend.tests import pdf_test_dicts



# Data dict names:
# COUNTY
# PLAINTIFF_#_# - Plaintiffs
# CASE_NO
# DEFENDANT_#_# - Defendants
# MOTION
# CASE
# DISMISSAL (true/false)
# RESTITUTION (true/false)
# MONEY (true/false)
# JUDGEMENT_DATE (true/false)
# DATE_OF_JUDGEMENT
# STIPULATION (true/false)
# TERMS (true/false)
# DATE_#
# NAME_PRINTED
# SIGNATURE1 exists, but should not be filled by this
# ADDRESS
# CITY_STATE_ZIP
# PHONE
# PLAINTIFF_ADDRESS_1, PLAINTIFF_ADDRESS_2, PLAINTIFF_ADDRESS_3
# DEFENDANT_NAME_#
# PLAINTIFF_ADDRESS_CITYSTATEZIP_PHONE -single line [Address    CityStateZip     PHONE]
# OBJECTION_DATE - don't fill

TEMPLATE_PATH = 'template.pdf'
OUTPUT_PATH = 'output.pdf'
PDF_FORM_LOCATION = 'src/backend/files/EvictionPDF.pdf'

@dataclass
class CreatePDF:

    def fit_address(self, address):
        first_line = 22
        second_line = 72
        third_line = 65
        first_line_string = ''
        second_line_string = ''
        third_line_string = ''
        address_list = address.split()
        for stuff in address_list:
            if len(stuff) > first_line:
                if len(stuff) > second_line:
                    if len(stuff) > third_line:
                        raise Exception("Plainiff address is too long")
                    else:
                        third_line_string += stuff + " "
                        third_line = third_line - len(stuff) - 1
                        continue
                else:
                    second_line_string += stuff + " "
                    second_line = second_line - len(stuff) - 1
                    continue
            else:
                first_line_string += stuff + " "
                first_line = first_line - len(stuff) - 1
                continue

        address_output = [first_line_string, second_line_string, third_line_string]
        return address_output

    def data_dict_to_pdf_dict(self, input_dict):
        address_list = self.fit_address(input_dict['plaintiff_address'])
        output = PDF_form_template(
            DEFENDANT_ADDRESS=input_dict['def_mailing_address'],
            CITY_STATE_ZIP=input_dict['city_state_zip'],
            COUNTY_1=input_dict['county_name'],
            COUNTY_2=input_dict['county_name'],
            PLAINTIFF_1_1=input_dict['plaintiff_line1'],
            PLAINTIFF_1_2=input_dict['plaintiff_line2'],
            PLAINTIFF_2_1=input_dict['plaintiff_line1'],
            PLAINTIFF_2_2=input_dict['plaintiff_line2'],
            DEFENDANT_1_1=input_dict['defendant_line1'],
            DEFENDANT_1_2=input_dict['defendant_line2'],
            DEFENDANT_1_3=input_dict['defendant_line3'],
            DEFENDANT_1_4=input_dict['defendant_line4'],
            DEFENDANT_2_1=input_dict['defendant_line1'],
            DEFENDANT_2_2=input_dict['defendant_line2'],
            DEFENDANT_2_3=input_dict['defendant_line3'],
            DEFENDANT_2_4=input_dict['defendant_line4'],
            DATE=str(datetime.date.today()),
            DATE_2=str(datetime.date.today()),
            DATE_3=str(datetime.date.today()),
            CASE=input_dict['case_name'],
            CASE_NO_1=input_dict['case_number'],
            CASE_NO_2=input_dict['case_number'],
            DEFENDANT_NAME_1=input_dict['defendant_line1'],
            DEFENDANT_NAME_2=input_dict['defendant_line1'],
            DEFENDANT_NAME_3=input_dict['defendant_line1'],
            DATE_OF_JUDGEMENT=input_dict['date_of_judgement'],
            PHONE=input_dict['phone_number'],
            PLAINTIFF_NAME=input_dict['plaintiff_line1'],
            DISMISSAL=input_dict['dismissal'],
            RESTITUTION=input_dict['restitution'],
            MONEY=input_dict['money'],
            JUDGEMENT=input_dict['judgement'],
            STIPULATION=input_dict['stipulation'],
            TERMS=input_dict['terms'],
            DO_NOT_FILL="",
            DO_NOT_CLICK=False,
            PLAINTIFF_ADDRESS_3=address_list[0],
            PLAINTIFF_ADDRESS_2=address_list[1],
            PLAINTIFF_ADDRESS_1=address_list[2]
        )
        return output

    def fill_pdf(self, input_pdf_path, output_pdf_path, data_dict):
        ANNOT_KEY = '/Annots'
        ANNOT_FIELD_KEY = '/T'
        ANNOT_VAL_KEY = '/V'
        ANNOT_RECT_KEY = '/Rect'
        SUBTYPE_KEY = '/Subtype'
        WIDGET_SUBTYPE_KEY = '/Widget'
        template_pdf = pdfrw.PdfReader(input_pdf_path)
        template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        for page in template_pdf.pages:
            annotations = page[ANNOT_KEY]
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        if key in data_dict.keys():
                            if type(data_dict[key]) == bool:
                                if data_dict[key] == True:
                                    annotation.update(pdfrw.PdfDict(
                                        AS=pdfrw.PdfName('Yes')))
                            else:
                                annotation.update(
                                    pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                                )
                                annotation.update(pdfrw.PdfDict(AP=''))

        pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

    def PDF_filler(self, input_dict):
        output = CreatePDF.data_dict_to_pdf_dict(self, input_dict)
        CreatePDF.fill_pdf(self, PDF_FORM_LOCATION,
                           "src/backend/files/"+input_dict['plaintiff_line1']+".pdf",
                           output)


taco = CreatePDF()
CreatePDF.PDF_filler(taco, pdf_test_dicts.test_dict_2)
