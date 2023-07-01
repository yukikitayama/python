import configparser

config = configparser.ConfigParser()
print("Read", config.read("config.ini"))

# DEFAULT doesn't appear
print("Sections: ", config.sections())

print(config["mariadb"]["host"])
print(config["mariadb"]["name"])
print(config["mariadb"]["user"])
print(config["mariadb"]["password"])

print(config.sections()[0])
print(config[config.sections()[0]])

print("Interpolation")
print(config["redis"]["dsn"])

# Write configuration file
config_write = configparser.ConfigParser()

config_write["DEFAULT"] = {"host": "some_host"}
config_write["DB"] = {
    "username": "yuki",
    "password": "some_password"
}

with open("config_write.init", "w") as f:
    config_write.write(f)


