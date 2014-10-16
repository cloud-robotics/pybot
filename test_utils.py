#!/usr/bin/env python
from bot_vision.image_utils import to_color, to_gray
from bot_utils.dataset_readers import KITTIStereoDatasetReader

def test_dataset(color=False, scale=1.0): 
    if color: 
        return KITTIStereoDatasetReader(directory='~/data/dataset/', sequence='08', 
                                        left_template='image_2/%06i.png', right_template='image_3/%06i.png', 
                                        start_idx=0, scale=scale)
    else: 
        return KITTIStereoDatasetReader(directory='~/data/dataset/', sequence='08', start_idx=0, scale=scale)

def test_image(color=True, scale=1.0, stereo=False): 
    for l,r in test_dataset(color=True).iter_stereo_frames(): 
        l = to_color(l) if color else to_gray(l)
        if not stereo: 
            return l
        else: 
            r = to_color(r) if color else to_gray(r)
            return l,r

def test_video(color=True, scale=1.0, stereo=False): 
    for l,r in test_dataset(color=True).iter_stereo_frames(): 
        l = to_color(l) if color else to_gray(l)
        if not stereo: 
            yield l
        else: 
            r = to_color(r) if color else to_gray(r)
            yield l,r

if __name__ == "__main__": 
    from bot_vision.imshow_utils import imshow_cv

    # Test dataset
    dataset = test_dataset()
    for l,r in test_dataset(scale=0.5).iter_stereo_frames(): 
        imshow_cv('left/right', np.vstack([l,r]))

    # Test image
    im = test_image(color=True)
    imshow_cv('image', im)    

    # Test video
    for im in test_video(color=True): 
        print im.shape, im.dtype
        imshow_cv('video', im)

    cv2.waitKey(0)
