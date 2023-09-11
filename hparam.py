class hparams:
    train_or_test = 'train'
    output_dir = 'logs/your_program_name'
    aug = None
    latest_checkpoint_file = 'checkpoint_latest.pt'
    total_epochs = 40
    epochs_per_checkpoint = 10
    batch_size = 32
    ckpt = None
    init_lr = 0.002
    scheduer_step_size = 20
    scheduer_gamma = 0.8
    debug = False
    mode = '2d'  # '2d or '3d'
    in_class = 1
    out_class = 1

    crop_or_pad_size = 256, 256, 1  # if 2D: 256,256,1  3D : 256 , 256 ,32
    patch_size = 128, 128, 1  # if 2D: 128,128,1   3D : 32 , 32 ,32++

    # for test
    patch_overlap = 4, 4, 0  # if 2D: 4,4,0

    fold_arch = '*.png'  # 3D : *.nii.gz   2D :png

    save_arch = '.png'  # 3D : *.nii.gz  2D :png

    source_train_dir = 'D:\segment\\2Ddata\data\\train\image'
    label_train_dir = 'D:\segment\\2Ddata\data\\train\mask'
    source_test_dir = 'D:\segment\\2Ddata\data\\val\image'
    label_test_dir = 'D:\segment\\2Ddata\data\\val\iask'

    output_dir_test = 'results/your_program_name'
