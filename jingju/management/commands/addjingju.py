from django.core.management.base import BaseCommand, CommandError
import csv
from jingju import models

class Command(BaseCommand):

    def process(line):
        pass

    def handle(self, *args, **options):
        fp = csv.DictReader(open(args[0]))

        last_title = ""
        last_number = 0
        disc = 0
        therel = None
        for l in fp:
            print l
            title = l["Title"]
            if title != "":
                number = int(l["#"])
                track_name = l["Track list (recordings)"]
                artist = l["Artist"]
                label = l["Label"]
                cat = l["Catalog number"]
                reldate = l["Release date"]
                recdate = l["Recording date"]
                barcode = l["Barcode"]
                if title != last_title:
                    disc = 0
                    therel = models.Release.objects.create(title=title, artist=artist, label=label, catno=cat, reldate=reldate, recdate=recdate, barcode=barcode)
                    last_title = title
                if number < last_number:
                    disc += 1
                if disc == 0:
                    disc += 1
                thetrack = models.Track.objects.create(release=therel, name=track_name, disc=disc, position=number, artists=artist)
                last_number = number

        #self.stdout.write()

