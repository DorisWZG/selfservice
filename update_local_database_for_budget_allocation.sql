/* Because URLs for budget allocation is changed, certain fields and names in database need to be changed as well */
/* Run the following SQL scripts to update database */

LOCK TABLES self_service.budget_allocation_pricemetrics WRITE;
ALTER TABLE self_service.budget_allocation_pricemetrics RENAME To self_service.asia_media_planning_pricemetrics;
UNLOCK TABLES;

LOCK TABLES self_service.budget_allocation_industry WRITE;
ALTER TABLE self_service.budget_allocation_industry RENAME To self_service.asia_media_planning_industry;
UNLOCK TABLES;

LOCK TABLES self_service.budget_allocation_channel WRITE;
ALTER TABLE self_service.budget_allocation_channel RENAME To self_service.asia_media_planning_channel;
UNLOCK TABLES;

LOCK TABLES self_service.django_content_type WRITE;
UPDATE self_service.django_content_type
SET app_label='asia_media_planning'
WHERE app_label='budget_allocation';
UNLOCK TABLES;