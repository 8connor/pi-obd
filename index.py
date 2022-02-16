import obd
import time

# obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.Async('/dev/cu.usbserial-113011152750')

# print(connection.supported_commands)

# a callback that prints every new value to the console
def new_rpm(r):
    print(r.value.to('psi'))


connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_rpm, force=True)
connection.start()

# print(supports)

# # the callback will now be fired upon receipt of new values
time.sleep(60)
connection.stop()