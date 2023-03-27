import os

from detectron2.data import MetadataCatalog
from detectron2.data.datasets.coco import register_coco_instances

RED = (255,0,0)

def register_back_chicken_keypoints_dataset(root):
    root = os.path.join(root, 'back_chicken_keypoints/coco_format')
    register_coco_instances("chicken_keypoints_train", {}, 
        os.path.join(root, "annotations/train.json"), 
        os.path.join(root, "images")
    )
    
    meta = MetadataCatalog.get('back_chicken_keypoints_train')
    meta.thing_classes = ['back_chicken']
    meta.keypoint_names =  ['p1','p2','p3','p4','p5']
    meta.keypoint_connection_rules = [['p1','p2',RED], ['p1','p3',RED],['p2','p4',RED],['p3','p5',RED]]


def register_toy_chicken_keypoints_dataset(root):
    root = os.path.join(root, 'ChickenToyKP')
    register_coco_instances("toy_chicken_keypoints_train", {}, 
        os.path.join(root, "coco_format_anns/train.json"), 
        os.path.join(root, "chickenv_frames")
    )
    
    meta = MetadataCatalog.get('toy_chicken_keypoints_train')
    meta.thing_classes = ['toy_chicken']
    meta.thing_colors = [(255,255,0)]
    meta.stuff_colors = [(255,255,0)]
    meta.keypoint_names = ['beak','comb','backofhead','chest','back','starttail','endtail','rightfoot','leftfoot']
    # meta.keypoint_flip_map = [[1,2], [2,3],[3,4],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]]
    # meta.keypoint_connection_rules = [] # TODO


def register_smartplant_single_dataset(root):
    root = os.path.join(root, 'smart_plant/front_2_class_new_COCO')
    splits = ['train', 'val', 'test']
    for split in splits:
        register_coco_instances("smartplant_single_{}_dataset".format(split), {},
                os.path.join(root, "annotations/instances_{}2017.json".format(split)),
                os.path.join(root, "{}2017".format(split))
        )

        meta = MetadataCatalog.get('smartplant_single_{}_dataset'.format(split))
        meta.thing_classes = ['normal', 'defect']
        meta.thing_colors = [(255,255,0), (255,0,255)]
        meta.stuff_colors = [(255,255,0), (255,0,255)]


def register_smartplant_overlap_dataset(root):
    root = os.path.join(root, 'smart_plant/front_2_class_overlap')
    splits = ['train', 'val', 'test']
    for split in splits:
        register_coco_instances("smartplant_overlap_{}_dataset".format(split), {},
                os.path.join(root, "annotations/instances_{}2017.json".format(split)),
                os.path.join(root, "{}2017".format(split))
        )

        meta = MetadataCatalog.get('smartplant_overlap_{}_dataset'.format(split))
        meta.thing_classes = ['normal', 'defect']
        meta.thing_colors = [(255,255,0), (255,0,255)]
        meta.stuff_colors = [(255,255,0), (255,0,255)]


_root = os.getenv("DETECTRON2_DATASETS", "datasets")
register_back_chicken_keypoints_dataset(_root)
register_toy_chicken_keypoints_dataset(_root)
register_smartplant_single_dataset(_root)
register_smartplant_overlap_dataset(_root)