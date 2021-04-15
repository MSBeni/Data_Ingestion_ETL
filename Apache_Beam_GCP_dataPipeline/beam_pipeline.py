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
# a method which is used in Map transformation. Map basically applies a simple one to one mapping function over each
# element in the collection. It means it just receive one row and its output is just one row.
def remove_last_colon(row):
    pass

# Write Transformation to clean the data in beam
# p collection is a unified storage of beam that store any batch or streaming data
cleaned_data = (
    p
    | beam.io.ReadFromText(input_pattern, skip_header_lines=1)
    | beam.Map(remove_last_colon)     # Map applies a simple one to one mapping func over each element in the collection
)