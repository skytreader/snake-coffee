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
