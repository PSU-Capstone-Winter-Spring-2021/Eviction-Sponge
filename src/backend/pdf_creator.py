import datetime
import io
from pathlib import Path

import pdfrw

# CreatePDF.fit_address fills the address lines by spacing out the words to fit without size reduction
# CreatePDF.data_dict_to_pdf_dict takes the data from the search function and spreads it out to the needed
#         form data dict. The PDF needs each form to have a separate name even if the data is the same :(
#         The template in form_filling can probably be removed or added to this, not sure which is better
# CreatePDF.fill_pdf does the actual work of filling the pdf with the data from the pdf dict. It looks odd,
#         but Adobe doesn't make this easy to automate.
# CreatePDF.create_form_name will name the pdf with the the name of the first defendant as
#         firstname_lastname.pdf
# CreatePDF.PDF_filler does is a wrapper that takes the initial input dict from search, does all of the work
#         then returns the absolute path to the pdf.
# Need to remember to add a one-liner to delete the file when the program exits or a new run is started.
# Something along the lines of 'file(filename).exists.os.remove()'


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
# JUDGMENT_DATE (true/false)
# DATE_OF_JUDGMENT
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
OUTPUT_PATH = 'output1.pdf'
PDF_FORM_LOCATION = Path('./files/EvictionPDF.pdf')


class CreatePDF:

    @staticmethod
    def fit_address(address):
        first_line = 22
        first_line_full = False
        second_line = 72
        second_line_full = False
        third_line = 65
        third_line_full = False
        first_line_string = ''
        second_line_string = ''
        third_line_string = ''
        address_list = address.split()
        for stuff in address_list:
            if len(stuff) > first_line or first_line_full:
                first_line_full = True
                if len(stuff) > second_line or second_line_full:
                    second_line_full = True
                    if len(stuff) > third_line or third_line_full:
                        third_line_full = True
                        # this is sticking everything extra on the third line; isn't optimal
                        third_line_string += stuff + ' '
                    else:
                        third_line_string += stuff + ' '
                        third_line = third_line - len(stuff) - 1
                        continue
                else:
                    second_line_string += stuff + ' '
                    second_line = second_line - len(stuff) - 1
                    continue
            else:
                first_line_string += stuff + ' '
                first_line = first_line - len(stuff) - 1
                continue

        address_output = [first_line_string, second_line_string, third_line_string]
        return address_output

    @staticmethod
    def data_dict_to_pdf_dict(input_dict):
        address_list = CreatePDF.fit_address(input_dict['plaintiff_address'])
        output = dict(
            COUNTY_1=input_dict['county_name'],
            PLAINTIFF_1_1=input_dict['plaintiff_line1'],
            PLAINTIFF_1_2=input_dict['plaintiff_line2'],
            CASE_NO_1=input_dict['case_number'],
            DEFENDANT_1_1=input_dict['defendant_line1'],
            DEFENDANT_1_2=input_dict['defendant_line2'],
            DEFENDANT_1_3=input_dict['defendant_line3'],
            DEFENDANT_1_4=input_dict['defendant_line4'],
            DEFENDANT_NAME_1=input_dict['defendant_line1'],
            CASE=input_dict['case_name'],
            DISMISSAL=input_dict['dismissal'],
            RESTITUTION=input_dict['restitution'],
            MONEY=input_dict['money'],
            #   JUDGMENT_DATE=input_dict['judgment_date'],
            DATE_OF_JUDGMENT=input_dict['date_of_judgment'],
            STIPULATION=input_dict['stipulation'],
            TERMS=input_dict['terms'],
            DATE_1=str(datetime.date.today().strftime('%m-%d-%Y')),
            DEFENDANT_NAME_2=input_dict['defendant_line1'],
            DEFENDANT_ADDRESS=input_dict['def_mailing_address'],
            CITY_STATE_ZIP=input_dict['city_state_zip'],
            PHONE=input_dict['phone_number'],
            DATE_2=str(datetime.date.today().strftime('%m-%d-%Y')),
            PLAINTIFF_ADDRESS_1=address_list[0],
            PLAINTIFF_ADDRESS_2=address_list[1],
            PLAINTIFF_ADDRESS_3=address_list[2],
            DATE_3=str(datetime.date.today().strftime('%m-%d-%Y')),
            DEFENDANT_NAME_3=input_dict['defendant_line1'],
            DO_NOT_FILL='',
            DO_NOT_CLICK=False
        )
        return output

    @staticmethod
    def fill_pdf(input_pdf_path, data_dict):
        ANNOT_KEY = '/Annots'
        ANNOT_FIELD_KEY = '/T'
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
                        if key in data_dict:
                            if type(data_dict[key]) == bool:
                                if data_dict[key] == True:
                                    annotation.update(pdfrw.PdfDict(
                                        AS=pdfrw.PdfName('On')))
                            else:
                                annotation.update(pdfrw.PdfDict(V='{}'.format(data_dict[key])))
                                annotation.update(pdfrw.PdfDict(AP=''))
        pdf_buffer = io.BytesIO()
        pdfrw.PdfWriter().write(pdf_buffer, template_pdf)
        pdf_buffer.seek(0)
        return pdf_buffer

    @staticmethod
    def create_form_name(input_dict):
        filename = input_dict['defendant_line1'].replace(' ', '_')
        filename = filename or 'FED-Motion-SetAside'
        filename = filename + '.pdf'
        return filename

    @staticmethod
    def PDF_filler(input_dict):
        pdf_dict = CreatePDF.data_dict_to_pdf_dict(input_dict)
        filename = CreatePDF.create_form_name(input_dict)
        pdf = CreatePDF.fill_pdf(PDF_FORM_LOCATION, pdf_dict)
        return pdf, filename

# taco = CreatePDF()
# taco.PDF_filler(pdf_test_dicts.test_dict_2)
