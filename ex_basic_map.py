from src.map_utils import create_map

project_path = "projects/public/sample/"

# generate map folder
create_map(
    datapointsPath=project_path+"data_in/datapoints.csv",
    linksPath=project_path+"data_in/edges.csv",
    datapointAttrPath=project_path+"data_in/datapoint_attrs.csv",
    node_attr_map={"OriginalLabel": "label", "OriginalX": "x_tsne", "OriginalY": "y_tsne"},
    link_attr_map={"source": "Source", "target": "Target", "isDirectional": "isDirectional"},
    outFolder="data_out",
)
