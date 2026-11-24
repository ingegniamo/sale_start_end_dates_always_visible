# Sale Start End Dates Always Visible

[![License: OPL-1](https://img.shields.io/badge/licence-OPL--1-F1972B)](https://www.odoo.com/documentation/user/18.0/legal/licenses/licenses.html)
[![Odoo](https://img.shields.io/badge/Odoo-18.0-F1972B)](https://www.odoo.com)
[![Maintained by STeSI](https://img.shields.io/badge/maintained%20by-STeSI%20Consulting-F1972B)](https://stesi.consulting)

Extension of the OCA module `sale_start_end_dates`: the date fields of the sale order lines are
always visible.

## Features

`sale_start_end_dates` shows the start date, end date and number of days of an order line only
when its product requires dates (`must_have_dates`). With this module the three fields are always
visible on:

- the order lines list of the sales order form;
- the read-only order line form.

The fields stay required only when the product requires dates, as in the OCA module.

## Technical notes

| Element | Detail |
|---|---|
| Views | `sale_start_end_dates.view_order_form` and `sale_start_end_dates.sale_order_line_view_form_readonly`: the `invisible` attribute of `start_date`, `end_date` and `number_of_days` is removed |
| Depends | `sale_start_end_dates` |
| Models, fields, data | none |

The module keeps the OCA module unchanged, so `sale_start_end_dates` can be updated from OCA
without losing the behaviour. On a copy of `sale_start_end_dates` that already shows the fields,
the module has no effect.

## Changelog

### 18.0.1.0.0

- First version: the date fields of the order lines are always visible, through view
  inheritance on the views of `sale_start_end_dates`.

## Credits

**Authors**

- STeSI Consulting

**Contributors**

- Daniele Lucarelli — lucarelli.d@stesi.consulting
