from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--dataset", type=str)
    args = parser.parse_args()

    print(f"make_arrow for {args.dataset}")

    if args.dataset == "coco":
        from meter.utils.write_coco_karpathy import make_arrow
        make_arrow("/share/dataset/vl_dataset/coco_captions", 
                   "/share/dataset/vl_dataset/coco_captions/coco_karpathy_arrow")

    if args.dataset == "sbu":
        from meter.utils.write_sbu import make_arrow

    if args.dataset == "vqa":
        from meter.utils.write_vqa import make_arrow
        make_arrow("/share/dataset/vl_dataset/coco_captions",
                   "/share/dataset/vl_dataset/coco_captions/vqa_arrows")
        
    print("finish")

        