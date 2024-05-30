import argparse
from dataclasses import dataclass
from atlas import AtlasClient


@dataclass
class Migration:
    name: str


class MigrationManager:
    def __init__(self, api_key: str, project_id: str):
        self.client = AtlasClient(api_key, project_id)

    def create_migration(self, migration: Migration):
        """Create a new migration"""
        self.client.create_migration(migration.name)
        print(f"Migration '{migration.name}' created successfully!")

    def apply_migration(self, migration: Migration):
        """Apply a migration"""
        if self.client.get_migration(migration.name):
            self.client.apply_migration(migration)
            print(f"Migration '{migration.name}' applied successfully!")
        else:
            print(f"Migration '{migration.name}' not found.")

    def list_migrations(self):
        """List all migrations"""
        migrations = self.client.list_migrations()
        if migrations:
            print("Existing Migrations:")
            for migration in migrations:
                print(f"- {migration.name}")
        else:
            print("No migrations found.")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Atlas Migration Manager")
    parser.add_argument("api_key", help="Atlas API key")
    parser.add_argument("project_id", help="Atlas project ID")
    parser.add_argument("command", choices=["create", "apply", "list"], help="Action to perform")
    parser.add_argument("--name", help="Name of the migration (required for 'create' and 'apply' commands)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    manager = MigrationManager(args.api_key, args.project_id)

    if args.command == "create" or args.command == "apply":
        if args.name:
            migration = Migration(args.name)
            if args.command == "create":
                manager.create_migration(migration)
            else:
                manager.apply_migration(migration)
        else:
            print(f"Error: '{args.command}' command requires a migration name.")
    elif args.command == "list":
        manager.list_migrations()


if __name__ == "__main__":
    main()
