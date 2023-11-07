SELECT e.email 
FROM public.email_table as e
JOIN public.data_table as d on e.join_id = d.join_id
WHERE MOD(d.column_1, 2) = 0
AND d.column_2 < d.column_1
AND MOD(d.column_3, 10) = 1






