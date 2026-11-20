import math

def blend_ir(early, late, t):
    """IR 插值。"""
    raise NotImplementedError("TODO: blend_ir")

def resample_ir(samples, ir_rate, engine_rate):
    """IR 重采样。"""
    raise NotImplementedError("TODO: resample_ir")

def doppler_delay(speed, base):
    """移动声源延迟。"""
    raise NotImplementedError("TODO: doppler_delay")

def path_occlusion(blocked):
    """路径遮挡。"""
    raise NotImplementedError("TODO: path_occlusion")

def portal_split(energy, ratio):
    """portal 能量分配。"""
    raise NotImplementedError("TODO: portal_split")

def downmix_center(center, left, right):
    """下混矩阵。"""
    raise NotImplementedError("TODO: downmix_center")

def short_reverb(late, quality):
    """降档短混响。"""
    raise NotImplementedError("TODO: short_reverb")

def pre_delay(room_size, speed):
    """预延迟。"""
    raise NotImplementedError("TODO: pre_delay")

def energy_crossfade(a, b, t):
    """能量交叉淡化。"""
    raise NotImplementedError("TODO: energy_crossfade")

def room_id(seed, index):
    """房间 id。"""
    raise NotImplementedError("TODO: room_id")

def early_reflection(distance, speed):
    """早期反射。"""
    raise NotImplementedError("TODO: early_reflection")

def late_decay(decay, time):
    """后期衰减。"""
    raise NotImplementedError("TODO: late_decay")

def ir_length(samples, rate):
    """IR 时长。"""
    raise NotImplementedError("TODO: ir_length")

def occlusion_gain(blocked, open):
    """遮挡增益。"""
    raise NotImplementedError("TODO: occlusion_gain")

def reverb_key(room, listener):
    """混响键。"""
    raise NotImplementedError("TODO: reverb_key")
