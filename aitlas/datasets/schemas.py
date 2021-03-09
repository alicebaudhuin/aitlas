from marshmallow import fields, validate

from ..base.schemas import BaseDatasetSchema


class GenericMulticlassDatasetSchema(BaseDatasetSchema):
    download = fields.Bool(
        missing=False, description="Whether to download the dataset", example=True
    )
    csv_file_path = fields.String(
        missing=None, description="CSV file on disk", example="./data/train.csv",
    )
    labels = fields.Dict(
        missing=None, description="Labels needed to tag the predictions.",
    )


class GenericMultiLabelsDatasetSchema(BaseDatasetSchema):
    root = fields.String(
        missing="/", description="Dataset path on disk", example="./data/BigEarthNet/"
    )


class SegmentationDatasetSchema(BaseDatasetSchema):
    root = fields.String(
        missing="/", description="Dataset path on disk", example="./data/BigEarthNet/"
    )
    csv_file_path = fields.String(
        missing=None, description="CSV file on disk", example="./data/train.csv",
    )
    transforms = fields.List(
        fields.String,
        missing=["aitlas.transforms.BaseSegmentation"],
        description="Classes to run transformations.",
    )


class BigEarthNetSchema(BaseDatasetSchema):
    csv_file_path = fields.String(
        missing=None, description="CSV file on disk", example="./data/train.csv"
    )
    lmdb_path = fields.String(required=True, description="Path to the lmdb storage")
    root = fields.String(
        required=True, description="Dataset path on disk", example="./data/BigEarthNet/"
    )
    import_to_lmdb = fields.Bool(
        missing=False, description="Should the data be moved to LMDB"
    )
    bands10_mean = fields.List(
        fields.Float,
        missing=[429.9430203, 614.21682446, 590.23569706],
        required=False,
        description="List of mean values for the 3 channels",
    )
    bands10_std = fields.List(
        fields.Float,
        missing=[572.41639287, 582.87945694, 675.88746967],
        required=False,
        description="List of std values for the 3 channels",
    )


class BreizhCropsSchema(BaseDatasetSchema):
    region = fields.String(
        missing=None, description="Brittany region (frh01..frh04)", example="frh01"
    )
    root = fields.String(
        required=True, description="Dataset path on disk", example="./breizhcrops_dataset"
    )
    year = fields.Integer(required=True, description="year")
    filter_length = fields.Integer(required=True, description="filter_length")
    level = fields.String(
        required=True, description="L1C or L2A", example="L1C"
    )
    verbose = fields.Bool(
        missing=False, description="verbose"
    )

    load_timeseries = fields.Bool(
        missing=False, description="load_timeseries"
    )    
    recompile_h5_from_csv = fields.Bool(
        missing=False, description="recompile_h5_from_csv"
    )    
    preload_ram = fields.Bool(
        missing=False, description="preload_ram"
    )
