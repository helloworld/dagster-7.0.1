from dagster import pipeline, solid, RepositoryDefinition, InputDefinition


@solid
def hello_world(context):
    context.log.info("Hello world")
    return 1


@solid(input_defs=[InputDefinition("number", int)])
def goodbye_world(context, number):
    context.log.info("Number: {}".format(number))
    context.log.info("Goodbye world")


@pipeline
def other_pipeline():
    goodbye_world(hello_world())


def define_repository():
    return RepositoryDefinition("my_repository", pipeline_defs=[other_pipeline])