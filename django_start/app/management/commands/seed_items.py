# yourapp/management/commands/seed_items.py
from django.core.management.base import BaseCommand
from app.models import Items
from pathlib import Path
import csv

class Command(BaseCommand):
    help = "Seed Items from inventory.csv (idempotent)."

    def handle(self, *args, **options):
        csv_path = Path(__file__).resolve().parents[2] / "inventory.csv"
        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV not found: {csv_path}"))
            return

        created, updated = 0, 0
        with open(csv_path, newline='') as f:
            for row in csv.DictReader(f):
                obj, was_created = Items.objects.update_or_create(
                    item_id=int(row["item_id"]),
                    defaults={
                        "name": row["name"],
                        "price": row["price"],
                        "quantity": row["quantity"],
                    },
                )
                created += int(was_created)
                updated += int(not was_created)

        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created: {created}, Updated: {updated}"))
