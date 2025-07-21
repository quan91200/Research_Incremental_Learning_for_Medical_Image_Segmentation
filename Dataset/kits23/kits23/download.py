"""A script to download the KiTS23 dataset into this repository"""
import sys
from tqdm import tqdm
from pathlib import Path
import urllib.request
import shutil
from time import sleep

from kits23 import TRAINING_CASE_NUMBERS
from urllib.error import ContentTooShortError


DST_PTH = Path(__file__).resolve().parent.parent / "dataset"


def get_destination(case_id: str, create: bool = False):
    destination = DST_PTH / case_id / "imaging.nii.gz"
    if create:
        destination.parent.mkdir(exist_ok=True)
    return destination


def cleanup(tmp_pth: Path, e: Exception):
    if tmp_pth.exists():
        tmp_pth.unlink()

    if e is None:
        print("\nInterrupted.\n")
        sys.exit()
    raise(e)


def download_case(case_num: int, pbar: tqdm, retry_count=3):
    remote_name = f"master_{case_num:05d}.nii.gz"
    url = f"https://kits19.sfo2.digitaloceanspaces.com/{remote_name}"
    destination = get_destination(f"case_{case_num:05d}", True)
    tmp_pth = destination.parent / f".partial.{destination.name}"

    try:
        urllib.request.urlretrieve(url, str(tmp_pth))
        shutil.move(str(tmp_pth), str(destination))
    except KeyboardInterrupt as e:
        pbar.close()
        while True:
            try:
                sleep(0.1)
                cleanup(tmp_pth, None)
            except KeyboardInterrupt:
                pass
    except (ContentTooShortError, Exception) as e:
        if retry_count > 0:
            print(f"\n[Retry] Failed to download case_{case_num:05d}. Retries left: {retry_count}")
            sleep(5)
            download_case(case_num, pbar, retry_count=retry_count - 1)
        else:
            print(f"\n❌ Giving up on case_{case_num:05d} after multiple retries.")
            pbar.close()
            while True:
                try:
                    cleanup(tmp_pth, e)
                except KeyboardInterrupt:
                    pass


def download_dataset():
    # Make output directory if it doesn't exist already
    DST_PTH.mkdir(exist_ok=True)

    # Giới hạn số lượng case tải
    LIMIT = 50
    left_to_download = [
        case_num for case_num in TRAINING_CASE_NUMBERS[:LIMIT]
        if not get_destination(f"case_{case_num:05d}").exists()
    ]

    print(f"\nFound {len(left_to_download)} cases to download\n")
    for case_num in (pbar := tqdm(left_to_download)):
        pbar.set_description(f"Downloading case_{case_num:05d}...")
        download_case(case_num, pbar)


if __name__ == "__main__":
    download_dataset()
