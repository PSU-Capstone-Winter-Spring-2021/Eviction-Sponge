from dataclasses import dataclass

import pdfrw
import datetime

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
@dataclass

class CreatePDF:

    TEMPLATE_PATH = 'template.pdf'
    OUTPUT_PATH = 'output.pdf'



    test_dict = {
        'COUNTY_1': 'Multnomah',
        'COUNTY_2': 'Multnomah',
        'PLAINTIFF_1_1': "The Burger King",
        'PLAINTIFF_1_2': "",
        'DEFENDANT_1_1': 'Hamburgler',
        'DEFENDANT_1_2': "Grimace",
        'DEFENDANT_1_3': "",
        'DEFENDANT_1_4': "",
        'PLAINTIFF_2_1': "The Burger King",
        'PLAINTIFF_2_2': "",
        'DEFENDANT_2_1': 'Hamburgler',
        'DEFENDANT_2_2': "Grimace",
        'DEFENDANT_2_3': "",
        'DEFENDANT_2_4': "",
        'MOTION': 'Hamburgler',
        'CASE': 'Burger King v Hamburgler',
        'CASE_NO_1': '8675309',
        'CASE_NO_2': '8675309',
        'DISMISSAL': False,
        'RESTITUTION': 'Yes',
        'MONEY': 'Yes',
        'JUDGEMENT': 'Yes',
        'STIPULATION': False,
        'TERMS': False,
        'DATE_OF_JUDGEMENT': '5/29/2015',
        'DATE': datetime.date.today(),
        'NAME_PRINTED': 'Hamburgler',
        'ADDRESS': '10050 SW Barbur Blvd',
        'CITY_STATE_ZIP': 'Portland OR, 97219',
        'PHONE': '(503) 246-6711',
        'DATE_2': datetime.date.today(),
        'PLAINTIFF_ADDRESS_1': '11539 SW',
        'PLAINTIFF_ADDRESS_2': 'Pacific Hwy',
        'PLAINTIFF_ADDRESS_3': 'Tigard, OR 97223',
        'DATE_3': datetime.date.today(),
        'DEFENDANT_NAME_1': "Hamburgler",
        'DEFENDANT_NAME_2': "Hamburgler",
        'DEFENDANT_ADDRESS': '10050 SW Barbur Blvd',
        'PLAINTIFF_NAME': "The Burger King",
        'DO_NOT_FILL': "",
        'DO_NOT_CLICK': False
    }

    def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
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

    fill_pdf("src/backend/files/Fillable_FED-Motion-SetAside-2020-01-01.pdf", "src/backend/files/test_result.pdf", test_dict)
