import matplotlib.pyplot as plt
from moabb.datasets import BNCI2014001
from moabb.paradigms import LeftRightImagery
from numpy import arange, array, concatenate, newaxis, linspace
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from pyriemann.tangentspace import TangentSpace
from pyriemann.utils.distance import distance_riemann
from pyriemann.utils.mean import mean_riemann


def get_raw_mne_data():
    dataset = BNCI2014001()
    sessions = dataset._get_single_subject_data(subject=1)
    raw_mne = sessions["session_T"]["run_1"]
    return raw_mne


def get_trials_data():
    dataset = BNCI2014001()
    paradigm = LeftRightImagery()
    X, labels, _ = paradigm.get_data(dataset=dataset, subjects=[1])
    return X, labels


def plot_signal(signal, sfreq, channels, electrode, n_seconds=2):
    time = linspace(0, n_seconds, n_seconds * sfreq).reshape((1, n_seconds * sfreq))
    fig, ax = plt.subplots()
    ax.plot(time.T, signal[channels == electrode, : n_seconds * sfreq].T, lw=0.5)
    ax.set_title("{}".format(electrode))
    ax.set_xlabel("time (s)")
    ax.set_ylabel(r"V")


def plot_signals(signal, sfreq, n_seconds=1):
    time = linspace(0, n_seconds, n_seconds * sfreq).reshape((1, n_seconds * sfreq))
    fig, ax = plt.subplots()
    ax.plot(time.T, signal[:-4, : n_seconds * sfreq].T, lw=0.5, color="C0", alpha=0.3)
    ax.set_title("All electrodes")
    ax.set_xlabel("time (s)")
    ax.set_ylabel(r"V")


def plot_cov(cov, labels, n=5):
    right = arange(len(labels))[labels == "right_hand"][-n:]
    left = arange(len(labels))[labels == "left_hand"][-n:]
    fig, axes = plt.subplots(2, n)
    for i, (r, l) in enumerate(zip(right, left)):
        axes[0, i].imshow(cov[r])
        axes[0, i].set_xticks([])
        axes[0, i].set_yticks([])
        axes[1, i].imshow(cov[l])
        axes[1, i].set_xticks([])
        axes[1, i].set_yticks([])
    axes[0, n // 2].set_title("Right hand")
    axes[1, n // 2].set_title("Left hand")
    plt.tight_layout()


def plot_cov_mean(cov, labels, n=5):
    right = arange(len(labels))[labels == "right_hand"][-n:]
    left = arange(len(labels))[labels == "left_hand"][-n:]
    mean_r = mean_riemann(cov[right])
    mean_l = mean_riemann(cov[left])
    fig, axes = plt.subplots(2, n + 1)
    for i, (r, l) in enumerate(zip(right, left)):
        axes[0, i].imshow(cov[r])
        axes[0, i].set_xticks([])
        axes[0, i].set_yticks([])
        dist = distance_riemann(cov[r], mean_r)
        axes[0, i].set_xlabel("{:g}".format(dist))
        axes[1, i].imshow(cov[l])
        axes[1, i].set_xticks([])
        axes[1, i].set_yticks([])
        dist = distance_riemann(cov[l], mean_l)
        axes[1, i].set_xlabel("{:g}".format(dist))
    axes[0, -1].imshow(mean_r, cmap="magma")
    axes[0, -1].set_title("Mean")
    axes[0, -1].set_xticks([])
    axes[0, -1].set_yticks([])
    axes[1, -1].imshow(mean_l, cmap="magma")
    axes[1, -1].set_xticks([])
    axes[1, -1].set_yticks([])

    axes[0, n // 2].set_title("Right hand")
    axes[1, n // 2].set_title("Left hand")
    plt.tight_layout()


def plot_cov_ts(cov, labels, n=50):
    right = arange(len(labels))[labels == "right_hand"][-n:]
    left = arange(len(labels))[labels == "left_hand"][-n:]
    mean_r = mean_riemann(cov[right])
    mean_l = mean_riemann(cov[left])

    ts = Pipeline(
        [
            ("mapping", TangentSpace(metric="riemann", tsupdate=False)),
            ("dim_reduc", PCA(n_components=2)),
        ]
    )
    ts.fit(concatenate((cov, mean_r[newaxis, ...], mean_l[newaxis, ...])))

    C_ts = ts.transform(concatenate((cov, mean_r[newaxis, ...], mean_l[newaxis, ...])))

    fig, ax = plt.subplots(1, 1)
    ax.set_title("Tangent space")
    ax.scatter(C_ts[left, 0], C_ts[left, 1], c="C0", alpha=0.3, label=r"$C_l$")
    ax.scatter(C_ts[right, 0], C_ts[right, 1], c="C1", alpha=0.3, label=r"$C_r$")
    ax.scatter(C_ts[-2, 0], C_ts[-2, 1], c="C1", label=r"mean right", marker="*", s=200)
    ax.scatter(C_ts[-1, 0], C_ts[-1, 1], c="C0", label=r"mean left", marker="*", s=200)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend()
