==========
cch Runner
==========
----------------------------------
Provide interface for cch Runners.
----------------------------------

This tool is in an early development stage.

Since ``semantic-release`` does not allow people to follow pedantic the most updated `Semantic Versioning`_ specification, I can't publish packages with version 0.x, so I publish new updates in a beta channel that has to be considered unstable, since any breaking change may arrive at any time. Fortunatly I have not so much time to spend in free-time development, so they will not be too much.

.. _`Semantic Versioning`: https://semver.org/#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase

How to develop
--------------

You must have Poetry installed on your system to resolve dependancies.

Ensure that your local pre-commit configuration is installed::

    python -m pre-commit install

How to use
----------

Download using::

    pip install cch-runner

Add as a Poetry dependancy using::

    poetry add cch-runner

This project is not in a stable release, stay updated!

.. TODO: Create a shareable configuration for other Runners.
