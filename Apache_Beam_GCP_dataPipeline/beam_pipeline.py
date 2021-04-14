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
