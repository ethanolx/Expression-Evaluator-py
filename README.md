# CA2 - Parse Trees

|   Name        |   Admin   |
|---------------|-----------|
|   Ethan Tan   |   2012085 |
|   Reshma      |   2011972 |

## Files Structure

```
CA2 ---- data ---- input.txt
     |         |-- output_1.txt (operator implementation group 1)
     |         `-- output_2.txt (operator implementation group 2)
     |
     |-- doc ---- CA2_Brief.pdf
     |        |-- inheritance_scheme.txt
     |        |-- report.docx
     |        `-- report.pdf
     |
     |-- src ---- utils ---- io_utils.py
     |        |          `-- mergesort.py
     |        |
     |        |-- __init__.py
     |        |-- exceptions.py
     |        |-- expression.py
     |        |-- lexer.py
     |        |-- math_node.py
     |        |-- node.py
     |        |-- operand_.py
     |        |-- operator_.py
     |        |-- parse_tree.py
     |        |-- print_orientation.py
     |        |-- temp_node.py
     |        |-- tokenizer.py
     |        |-- tree_traversal_order.py
     |        `-- tree.py
     |
     |-- config.txt
     |-- main.py
     `-- README.md
```

## Setup

No setup is required besides a Python installation.

This project has no dependencies.

## Run Program

With default configuration file `config.txt`:

```console
python main.py
```

With another configuration file:

```console
python main.py path/to/config/file.txt
```

## See Also

- Assignment Brief: `doc/CA2_Brief.pdf`
- Inheritance Scheme: `doc/inheritance_scheme.txt`
- Report: `doc/report.docx` / `doc/report.pdf`