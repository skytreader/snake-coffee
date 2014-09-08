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

# exceptions.py

Creating your own Exceptions in Java is tedious. Most of the time, it's
sufficient to just override a bunch of constructors and then poof! The only
variable thing is the package name and the class name.

Hence this script! Just pass a JSON object of the form

    {
        "package":"net.skytreader.kode",
        "class":"TheOnlyException"
    }

And you get all your constructors overriden for you.
