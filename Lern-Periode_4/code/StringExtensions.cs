namespace imaginary_schooldatabase
{
    public static class StringExtensions
    {
        public static string ToUpper(this string value, int index)
        {
            char[] chars = value.ToCharArray();
            chars[index] = chars[index].ToUpper();

            return new string(chars);
        }
    }
}
