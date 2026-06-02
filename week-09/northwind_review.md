\# Northwind Review Notes



\## Customers Table



Primary Key:

\- CustomerID



Parent Tables:

\- None



Notes:

\- One row represents one customer.



\## Customers Table



| Column     | Represents           | PK?| FK?| Keep?| Better Name?    | Data Type| Possible Use        |

|------------|----------------------|----|----|------|-----------------|----------|---------------------|

| CustomerID | Unique identifier    | Yes| No | Yes  | CustomerID      | Text     | Relationships       |

| CompanyName| Customer company name| No | No | Yes  | Customer        | Text     | Grouping, filtering |

| ContactName| Main contact person  | No | No | Yes  | Contact Name    | Text     | Reporting           |

| Address    | Street address       | No | No | No   | Address         | Text     | Not useful          |

| City       | Customer city        | No | No | Yes  | Customer City   | Text     | Geography analysis  |

| Country    | Customer country     | No | No | Yes  | Customer Country| Text     | Geography analysis  |

| Phone      | Customer phone number| No | No | No   | Phone           | Text     | Not useful          |

