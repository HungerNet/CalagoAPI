from enum import StrEnum


class BackupDisk(StrEnum):
    BTRFS = "btrfs"
    DDUP_BAK = "ddup-bak"
    KOPIA = "kopia"
    LOCAL = "local"
    PROXMOX_BACKUP_SERVER = "proxmox-backup-server"
    RESTIC = "restic"
    S3 = "s3"
    ZFS = "zfs"

    def __str__(self) -> str:
        return str(self.value)
