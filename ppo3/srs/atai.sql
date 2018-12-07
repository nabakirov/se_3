create trigger CheckInsert 
  ON dbo.[Proizvodstvo] FOR INSERT as
  DECLARE @count_proiz FLOAT
  DECLARE @sum_proiz FLOAT = 0
  DECLARE @id_proiz FLOAT

  DECLARE @UpdateCountSurie FLOAT
  DECLARE @UpdateSummSurie FLOAT
  DECLARE @UpdateIdSurie int
  DECLARE @ListOfsurie int
  DECLARE @ListOfsurieInProiz int
  

  DECLARE @UpdateCountProiz FLOAT
  DECLARE @UpdateSummProiz FLOAT
  DECLARE @UpdateIzProiz int
  DECLARE @ListOfProiz int


  SELECT @count_proiz = (SELECT [count]  from inserted)
  SELECT @id_proiz = (SELECT produciz  from inserted)
  
  Select @ListOfsurie = (SELECT Count(Ingredient.Surie) 
  from Ingredient join surie on surie.ID = Ingredient.Surie
  where producie = @id_proiz and surie.[count] >= Ingredient.[count]*@count_proiz)

  Select @ListOfsurieInProiz = (SELECT Count(Ingredient.Surie) 
  from Ingredient 
  where producie = @id_proiz )

  Select @sum_proiz = (SELECT SUM(Ingredient.[count]* @count_proiz* (Surie.summ / Surie.[count] )) 
  from Ingredient join surie on surie.ID = Ingredient.Surie
  where producie = @id_proiz and surie.[count] >= Ingredient.[count]*@count_proiz)

IF @ListOfsurie < @ListOfsurieInProiz 
begin
raiserror('ÕÂ ‰ÓÒÚ‡ÚÓ˜ÌÓ ÂÒÛÒÓ‚ ‰Îˇ ÔÓËÁ‚Ó‰ÒÚ‚‡ ‰‡ÌÌÓ„Ó ÔÓ‰ÛÍÚ‡.', 16, 1)
ROLLBACK
end

IF @ListOfsurie >= @ListOfsurieInProiz 
begin
Update 
	  Surie 
set 
	  [count] = (Surie.[count] - Ingredient.[count] * @count_proiz),
	  summ = (Surie.summ - (Ingredient.[count]* @count_proiz * (Surie.summ / Surie.[count] )))
from 
	  surie join Ingredient on Ingredient.Surie = surie.ID

Update 
	  GotovayProduci 
set 
	  [count] = (GotovayProduci.[count] + @count_proiz),
	  summ = GotovayProduci.[summ] + @sum_proiz
from 
	  GotovayProduci where GotovayProduci.id = @id_proiz
end




ON [dbo].[Production] FOR INSERT as
  DECLARE @countProduction FLOAT
  DECLARE @summProduction FLOAT = 0
  DECLARE @idProductinProduction FLOAT

  DECLARE @ListOFRaw int
  DECLARE @ListOFRawInProduction int

  SELECT @countProduction = (SELECT Count from inserted)
  SELECT @idProductinProduction = (SELECT Product  from inserted)

  Select @ListOFRaw = (SELECT Count(Ingredients.Raw)
  from Ingredients join RawMats on RawMats.ID = Ingredients.Raw
  where Product = @idProductinProduction and RawMats.[Count] >= Ingredients.[Count]*@countProduction)

  Select @ListOFRawInProduction = (SELECT Count(Ingredients.Raw)
  from Ingredients
  where Product = @idProductinProduction )

  Select @summProduction = (SELECT SUM(Ingredients.[Count]* @countProduction* (RawMats.Summ / RawMats.[Count] ))
  from Ingredients join RawMats on RawMats.ID = Ingredients.Raw
  where Product = @idProductinProduction and RawMats.[Count] >= Ingredients.[Count]*@countProduction)

IF @ListOFRaw < @ListOFRawInProduction
begin
raiserror('Не достаточно ресурсов для производства данного продукта.', 16, 1)
ROLLBACK
end

IF @ListOFRaw >= @ListOFRawInProduction
begin
Update
    RawMats
set
    [Count] = (RawMats.[Count] - Ingredients.[Count] * @countProduction),
    Summ = (RawMats.Summ - (Ingredients.[Count]* @countProduction * (RawMats.Summ / RawMats.[Count] )))
from
    RawMats join Ingredients on Ingredients.Raw = RawMats.ID

Update
    ComplatedProds
set
    [Count] = (ComplatedProds.Count + @countProduction),
    Summ = ComplatedProds.Summ + @summProduction
from
    ComplatedProds where ComplatedProds.id = @idProductinProduction
end