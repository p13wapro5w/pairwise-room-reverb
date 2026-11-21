import math


def blend_ir(early, late, t):
    """IR 插值：按声源位置在 early/late 之间线性插值，区域切换不再硬切。"""
    return early * (1.0 - t) + late * t


def resample_ir(samples, ir_rate, engine_rate):
    """IR 重采样：按引擎采样率换算样本数，避免尾巴时长偏移。"""
    return round(samples * engine_rate / ir_rate)


def doppler_delay(speed, base):
    """移动声源延迟：多普勒同时缩放延迟，不只改音高。"""
    return base / (1.0 + speed)


def path_occlusion(blocked):
    """路径遮挡：按传播路径判断，被挡路径增益为 0。"""
    return 0.0 if blocked else 1.0


def portal_split(energy, ratio):
    """portal 能量分配：两侧按 ratio 分配，总量守恒。"""
    return (energy * ratio, energy * (1.0 - ratio))


def downmix_center(center, left, right):
    """下混矩阵：中置按 0.5 计入，避免 5.1 下混时重复计能量。"""
    return left + right + 0.5 * center


def short_reverb(late, quality):
    """降档短混响：保留 25% 短尾巴而不是直接关掉 late。"""
    return late * (0.25 + 0.75 * quality)


def pre_delay(room_size, speed):
    """预延迟：按房间尺寸推导，小房间不与直达声重叠。"""
    return room_size / speed


def energy_crossfade(a, b, t):
    """能量交叉淡化：按能量（平方）归一，中点不掉能量。"""
    return math.sqrt(a * a * (1.0 - t) + b * b * t)


def room_id(seed, index):
    """房间 id。"""
    return f"{seed}:{index}"


def early_reflection(distance, speed):
    """早期反射：独立于 late 建模，按路径距离/声速求到达时间。"""
    return distance / speed


def late_decay(decay, time):
    """后期衰减：指数衰减包络。"""
    return math.exp(-decay * time)


def ir_length(samples, rate):
    """IR 时长（秒）。"""
    return samples / rate


def occlusion_gain(blocked, open):
    """遮挡增益：路径被挡为 0，否则取开放路径增益。"""
    return 0.0 if blocked else open


def reverb_key(room, listener):
    """混响键。"""
    return f"{room}:{listener}"
