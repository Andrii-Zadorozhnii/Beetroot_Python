SELECT departments.depart_name,
       countries.country_name
FROM departments
         JOIN locations ON departments.location_id == locations.location_id
         JOIN countries ON locations.country_id == countries.country_id
WHERE country_name == 'Italy'
   OR country_name == 'United Kingdom'
