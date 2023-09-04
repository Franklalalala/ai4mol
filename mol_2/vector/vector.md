vector

|                 | cutoff     | max_lr     | is_vector     | iid       | ood        |
| --------------- | ---------- | ---------- | ------------- | --------- | ---------- |
| dc_painn_old    | 20         | 1e-3       | false         | 3.076     | 3.119      |
| dc_trail_vector | 8          | 1e-3       | True          | NAN       | NAN        |
| dc_8            | 8          | 5e-4       | True          | *3.042*   | *3.106*    |
| dc_20           | 20         | 5e-4       | True          | 3.123     | *3.106*    |
| dc_leftnet      | 8          | 5e-4       | false         | **2.927** | **3.039**  |
|                 | **cutoff** | **max_lr** | **is_vector** | **iid**   | **ood**    |
| vs_painn_old    | 20         | 5e-4       | false         | *5.972*   | *12.832*   |
| vs_8            | 8          | 5e-4       | True          | 5.999     | 13.022     |
| vs_20           | 20         | 5e-4       | True          | 6.252     | 13.197     |
| vs_leftnet      | 8          | 5e-4       | false         | **5.706** | **12.433** |



