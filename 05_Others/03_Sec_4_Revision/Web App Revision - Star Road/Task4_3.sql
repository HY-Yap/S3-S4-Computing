SELECT RelicSet.Name AS 'Set Name', COUNT(Relic.ID) AS 'Count'
FROM RelicSet
INNER JOIN Relic
ON RelicSet.ID = Relic.SetID
GROUP BY RelicSet.ID
ORDER BY COUNT DESC
