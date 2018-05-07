/* Query relevant warc filenames for food-related corpus from Common Crawl's columnar index */
/* Uses Amazon Athena */

select url,warc_filename, warc_record_offset, warc_record_length
from ccindex
where 
crawl = 'CC-MAIN-2018-13'
and fetch_status < 400
and url_host_tld in ('com', 'br', 'au', 'ca', 'net', 'gov', 'edu', 'co', 'co.uk', 'uk','blog', 'ai','us')
and (url_host_2nd_last_part like '%food%' OR
     url_host_2nd_last_part like '%nutrition%' OR
     url_host_2nd_last_part like '%meal%' OR
     url_host_2nd_last_part like '%recipe%' OR
     url_host_2nd_last_part like '%diet%' OR
     url_host_2nd_last_part like '%healthy%' OR
     url_host_2nd_last_part like '%ingredients%' OR
     url_host_2nd_last_part like '%vegetables%' OR
     url_host_2nd_last_part like '%mealplan%')
and subset = 'warc'
     