import torch

def flatten(x, key='', res=None):
    if res is None:
        res = dict()
    if isinstance(x, list):
        for i, y in enumerate(x):
            flatten(y, f'{key}/{i}', res)
    elif isinstance(x, dict):
        for k, y in x.items():
            flatten(y, f'{key}/{k}', res)
    else:
        res[key] = x
    return res

ckpt_file = "Models/Kokoro/kokoro-ddc-May-16-2021_01+39PM-08a4dab/checkpoint_130000.pth.tar"
ckpt = torch.load(ckpt_file, map_location="cpu")

for k, v in ckpt.items():
    if isinstance(v, torch.Tensor):
        if len(v.shape) > 1 and v.shape[0] == 182:
            print(k, v.shape)

l = 66 # 130
ckpt['model']['embedding.weight'] = ckpt['model']['embedding.weight'][:l, :]
ckpt['optimizer']['state'][0]['exp_avg'] = ckpt['optimizer']['state'][0]['exp_avg'][:l, :]
ckpt['optimizer']['state'][0]['exp_avg_sq'] = ckpt['optimizer']['state'][0]['exp_avg_sq'][:l, :]

torch.save(ckpt, 'data/tts_model.pth.tar')