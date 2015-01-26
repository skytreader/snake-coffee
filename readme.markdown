# snake coffee

For the Java terminal afficionado. Generate boilerplate Java code with the help
of these scripts. Talk with the scripts via JSON.

# builder.py

Generates Plain Old Java Objects (POJO) available for construction via the
Builder pattern as described in Joshua Bloch's _Effective Java 2e_.

Check `java-object.json` for an example.

Some notes:

 - For the `fields` map, the `"required": true` flag can be absent if field is
   not required. However, _all_ optional fields require the `default` key.
 - If the type (and, consequently, default) is not a primitive (or a member of 
   `java.lang`) you can still use this like so

        "myOwnField": {"type":"OwnType", "default":"new OwnType()"}

# exception.py

Creating your own Exceptions in Java is tedious. Most of the time, it's
sufficient to just override a bunch of constructors and then poof! The only
variable thing is the package name and the class name.

Hence this script! Just pass a JSON object of the form

    {
        "package":"net.skytreader.kode",
        "class":"TheOnlyException"
    }

And you get all your constructors overriden for you.

# config.py

Creates a **config object** for (no one else but) you.

Config object is a pattern I use to deal with config files. Let a class represent
the config file. Pass the config file's pathname to the constructor and methods
to access the contents of the config file is provided by the object.

Often as I develop, I may decide to change how the behavior of a system is
derived from the config file or change the structure of the config file. This
pattern allows for such changes to be as transparent as possible to the rest of
the code.

Say, for instance, I have two config fields `app_port` and `db_port`:

    public int getAppPort(){
        return Integer.parseInt(configFile.getProperty("app-port"));
    }

    public int getDbPort(){
        return Integer.parseInt(configFile.getProperty("db-port"));
    }

Then, I suddenly decide to make it that `db_port` is always +10 of the value
of `app_port` (debate as to the merits of this "decision" is moot since this _is
just an example_). Without the config object, I would have to search through my
code for wherever I had need for `db_port` and adjust it accordingly. With
config object, I can just

    public int getDbPort(){
        return getAppPort() + 10;
    }

And no other call ever need to be bothered.

Config object also has the advantage that if you decide to deprecate a config
field, you don't have to grep through your whole code base just to find where
the deprecated config field was used. You can just delete the corresponding
method in the config object, compile, and _voila!_---you have a list of where
the config field was used.

`config.json` is an example of the expected config file to be passed to this
script. The structure is as follows:

    {
        "package":"net.skytreader.kode",
        "config-fields":[]
    }

The expected contents of `config-field` are JSON dictionaries with the following
format:

    {
        "field-name":"app-port",
        "return-type":"int",
    }

The output class is named `ConfigReader`.
