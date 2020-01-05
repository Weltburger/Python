def get_frames(sg, sz, ovlp):
    step = int(sz * ovlp)
    print('Step: {}'.format(step))
    i = 0
    while i < len(sg):
        print(sg[i:i + sz])
        i = i + step


signal = [i for i in range(0, 1024)]
size = 15
overlap = 0.5
get_frames(signal, size, overlap)
