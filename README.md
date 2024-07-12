Gitus
=====

Gitus is a Python CLI tool designed for managing global Git users. It simplifies the process of switching between different global Git user configurations, making it easier for developers who work on multiple projects with different user credentials.

Features
--------

*   Add new global Git users
*   Remove existing global Git users
*   List all configured global Git users
*   Switch between different global Git users

Installation
------------

### Prerequisites

*   Python 3.x must be installed on your system.
*   Git must be installed and configured on your system.

### Clone the Repository

bash

Copy code

`git clone https://github.com/CrazyRag778/Gitus.git cd Gitus`

Usage
-----

### General Help

To get general usage help, run:

bash

Copy code

`py gitus help`

### User Management Help

To get help on managing users, run:

bash

Copy code

`py gitus help user`

### List Users

To list all configured global Git users, run:

bash

Copy code

`py gitus list`

Commands
--------

### Add a New User

To add a new global Git user, use the following command:

bash

Copy code

`py gitus add <username> <email>`

### Remove an Existing User

To remove an existing global Git user, use the following command:

bash

Copy code

`py gitus remove <username>`

### Switch User

To switch between different global Git users, use the following command:

bash

Copy code

`py gitus switch <username>`

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

### Steps to Contribute

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature-branch`)
3.  Commit your changes (`git commit -m 'Add some feature'`)
4.  Push to the branch (`git push origin feature-branch`)
5.  Open a Pull Request

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Contact
-------

For any questions or suggestions, feel free to contact:

*   **Dibyojit Datta**
*   GitHub: [CrazyRag778](https://github.com/CrazyRag778)
