-- 1.List the campuses by the most number of attendees from cohort 12
--  Not Completely doable due to the fact that there is no attendance registered per cohort
SELECT
  C.name,
  SUM(E.attendees),
  CO.name
FROM
  campus AS C
  JOIN event_campus AS EC ON C.id = EC.campus_id
  JOIN event AS E ON EC.event_id = E.id
  JOIN event_cohort AS EVCO ON E.id = EVCO.event_id
  JOIN cohort AS CO ON EVCO.cohort_id = CO.id
WHERE
  CO.name = "C12"
GROUP BY(C.name);
-- 6.Sort the users by the amount of unique events that they have given (unique event type)
SELECT
  USER_NAME,
  COUNT(*)
FROM
  (
    SELECT
      U.name AS USER_NAME,
      ET.name AS EVENT_TYPE
    FROM
      user AS U
      JOIN event_user AS EU ON U.id = EU.user_id
      JOIN event AS E ON EU.event_id = E.id
      JOIN event_type AS ET ON E.type = ET.id
    GROUP BY
      ET.name
  ) AS SUBQ
GROUP BY
  USER_NAME
ORDER BY
  COUNT(*) DESC;
-- 9.List the events with unique type that have only been given to 1 cohort
SELECT
  E.name AS EVENT_NAME,
  ET.name AS EVENT_TYPE,
  COUNT(*) AS REPETITIONS,
  C.name AS COHORT
FROM
  event_type AS ET
  JOIN event AS E ON ET.id = E.type
  JOIN event_cohort AS EVCO ON E.id = EVCO.event_id
  JOIN cohort AS C ON EVCO.cohort_id = C.id
GROUP BY
  ET.name
HAVING
  REPETITIONS = 1;
-- 12.List all events which name contains “sh”
SELECT
  name
from
  event
WHERE
  name LIKE '%sh%';
-- 13.Count events given per cohort and in total to all cohorts
  WITH query AS (
    SELECT
      C.name AS COHORT,
      COUNT(*) AS NUMBER_OF_EVENT
    FROM
      event AS E
      JOIN event_cohort AS EVCO ON E.id = EVCO.event_id
      JOIN cohort AS C ON EVCO.cohort_id = C.id
    GROUP BY
      COHORT
  )
SELECT
  *
FROM
  query
UNION
SELECT
  'Total',
  SUM(NUMBER_OF_EVENT)
FROM
  query;
-- 15.Obtain all the unique companies that have given an event at any time
SELECT
  CO.name
FROM
  company AS CO
  JOIN user AS U ON CO.id = U.id_company
  JOIN event_user AS EU ON U.id = EU.user_id
  JOIN event AS E ON EU.event_id = E.id
GROUP BY
  CO.name;
-- 17.List the amount of unique companies that have given events to each campus and cohort
SELECT
  *
FROM
  company AS CO
  JOIN user AS U ON CO.id = U.id_company
  JOIN event_user AS EU ON U.id = EU.user_id
  JOIN event AS E ON EU.event_id = E.id
  JOIN event_cohort AS EVCO ON E.id = EVCO.event_id
  JOIN cohort AS C ON EVCO.cohort_id = C.id
GROUP BY
  CO.name,
  C.name;