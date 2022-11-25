"""
This module introduce Runner class you can extend creating a new Runner based on your language or your specification.

.. note:
    Other users may contribute to the project providing a way to generate a
    template (pre-configurated with semantic-release?) to get in touch in a
    second creating a new interesting Runner plugin for cch.
"""


from typing import Any


class Runner:
    """
    Extendible class to run a project for cch tool.

    Provide a common interface for every other runner around.
    """

    def can_run(self) -> bool:
        """
        Run all necessary checks to ensure the applicability of this plugin.

        :return: True if checks are successful, false otherwise.
        :rtype: bool
        """
        raise NotImplementedError("Plugin.can_run")

    def run(self, inputs: Any, **kwargs) -> int:
        """
        Run the project using this Runner.

        :param inputs: Any input your runner could manage.
        :type inputs: Any

        :returns: Run result.
        :rtype: int

        .. warning:
            raise NotImplementedError when client didn't implement this function.
        """
        # Fix https://github.com/jendrikseipp/vulture#handling-false-positives
        # Make Vulture ignore unused kwargs var.
        del inputs
        raise NotImplementedError("Plugin.run", *kwargs)
