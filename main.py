from rental_listings import RentalListings
from csv_generator import CSVGenerator
import time

init = RentalListings()
details = init.get_links()
print(details)
time.sleep(3)

csv = CSVGenerator(details)
csv.fill_in_form()
