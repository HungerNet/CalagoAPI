from enum import StrEnum


class BackupAdapter(StrEnum):
    BTRFS = "btrfs"
    DDUP_BAK = "ddup-bak"
    KOPIA = "kopia"
    PROXMOX_BACKUP_SERVER = "proxmox-backup-server"
    RESTIC = "restic"
    S3 = "s3"
    WINGS = "wings"
    ZFS = "zfs"

    def __str__(self) -> str:
        return str(self.value)
