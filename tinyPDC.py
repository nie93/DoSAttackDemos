from pypmu.pdc import Pdc
from pypmu.frame import DataFrame

"""
tinyPDC will connect to pmu_ip:pmu_port and send request
for header message, configuration and eventually
to start sending measurements.
"""


if __name__ == "__main__":

    pdc = Pdc(pdc_id=9, pmu_ip="192.168.1.119", pmu_port=4712)
    pdc.logger.setLevel("DEBUG")

    pdc.run()  # Connect to PMU

    header = pdc.get_header()  # Get header message from PMU
    config = pdc.get_config()  # Get configuration from PMU

    pdc.start()  # Request to start sending measurements

    while True:

        data = pdc.get()  # Keep receiving data

        if type(data) == DataFrame:
            print(data.get_measurements())

        if not data:
            pdc.quit()  # Close connection
            break
