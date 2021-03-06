ALTER TABLE avtolux_pages
ADD COLUMN prev_elem INTEGER NULL
REFERENCES avtolux_pages(id);

-- store ordering by id
WITH
	sorted AS (
		SELECT ROW_NUMBER() OVER (ORDER BY id ASC) AS pos, id
		FROM avtolux_pages
		ORDER BY id ASC
	),
	merge AS (
		SELECT sorted.id AS id, shifted.id AS next_id
		FROM sorted
		LEFT JOIN sorted AS shifted ON (shifted.pos = sorted.pos - 1)
	)
UPDATE avtolux_pages SET prev_elem = merge.next_id
FROM merge
WHERE avtolux_pages.id = merge.id;
