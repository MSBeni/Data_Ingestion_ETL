import apache_beam as beam
# import the packages PipelineOptions and StandardOptions for standard configurations like executing the pipeline
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse


# ######################## Mandatory Part to run any Beam pipeline ########################################
parser = argparse.ArgumentParser()

parser.add_argument('--input', dest='input', required=True, help='input file to process.')

# pipeline_args will hold the environmental args and path_args will hold the import file location
path_args, pipeline_args = parser.parse_known_args()


input_pattern = path_args.input
options = PipelineOptions(pipeline_args)

p = beam.Pipeline(options=options)
############################################################################################################


def remove_last_colon(row):
    """
    a method which is used in Map transformation. Map basically applies a simple one to one mapping function over each
    element in the collection. It means it just receive one row and its output is just one row. This function will
    split each row based on , and then remove the : and join the material again
    :param row:
    :return:
    """
    cols = row.split(',')
    item = str(cols[4])

    if item.endswith(':'):
        cols[4] = item[:-1]

    return ','.join(cols)


def remove_special_characters(row):
    """
    remove the special characters from the rows
    :param row:
    :return:
    """
    import re
    cols = row.split(',')
    ret = ''
    for col in cols:
        clean_col = re.sub(r'[?%&]', '', col)
        ret = ret + clean_col + ','
    ret = ret[:-1]
    return ret

# Write Transformation to clean the data in beam
# p collection is a unified storage of beam that store any batch or streaming data
cleaned_data = (
    p
    | beam.io.ReadFromText(input_pattern, skip_header_lines=1)
    | beam.Map(remove_last_colon)     # Map applies a simple one to one mapping func over each element in the collection
    | beam.Map(lambda row: row.lower())
    | beam.Map(remove_special_characters)
    | beam.Map(lambda row: row + ',1')
)
# Now wee need to write the deliver status item in one table and the rest in another table
# so we need to store these two types of the data into two p collections, the first would be delivered_orders
# You can provide a unique label to any p transform, you cannot use two transformation in same code without providing
# any unique label to it
delivered_orders = (
    cleaned_data
    | 'delivered filter' >>
)