import tensorflow as tf
import sys
sys.path.insert(0, '/')

import hparamBASED as Hparam

# import hparamBASED as hparam
# ini doang yg trouble

# Default hyperparameters:
hparams = Hparam.HParams(
    # Comma-separated list of cleaners to run on text prior to training and eval. For non-English
    # text, you may want to use "basic_cleaners" or "transliteration_cleaners" See TRAINING_DATA.md.
    cleaners='english_cleaners',
    use_cmudict=False,  # Use CMUDict during training to learn pronunciation of ARPAbet phonemes

    # Audio:
    num_mels=80,
    num_freq=1025,
    sample_rate=20000,
    frame_length_ms=50,
    frame_shift_ms=12.5,
    preemphasis=0.97,
    min_level_db=-100,
    ref_level_db=20,

    # Model:
    # TODO: add more configurable hparams
    outputs_per_step=5,
    padding_idx=None,
    use_memory_mask=False,

    # Data loader
    pin_memory=True,
    num_workers=2,

    # Training:
    batch_size=32,
    adam_beta1=0.9,
    adam_beta2=0.999,
    initial_learning_rate=0.002,
    decay_learning_rate=True,
    nepochs=1000,
    weight_decay=0.0,
    clip_thresh=1.0,

    # Save
    checkpoint_interval=5000,

    # Eval:
    max_iters=200,
    griffin_lim_iters=60,
    power=1.5,              # Power to raise magnitudes to prior to Griffin-Lim
)


def hparams_debug_string():
    values = hparams.values()
    hp = ['  %s: %s' % (name, values[name]) for name in sorted(values)]
    return 'Hyperparameters:\n' + '\n'.join(hp)
