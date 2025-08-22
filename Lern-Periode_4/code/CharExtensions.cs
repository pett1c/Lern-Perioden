namespace imaginary_schooldatabase
{
    public static class CharExtensions
    {
        // ебанутый какой-то член (хз, даня про члены начал говорить)
        public static char ToUpper(this char character)
        {
            return character.ToString().ToUpper().ElementAt(0);
        }
        // конец ебанутых членов! ура!
    }
}
