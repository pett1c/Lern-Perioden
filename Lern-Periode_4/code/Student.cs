namespace imaginary_schooldatabase
{
    public class Student
    {
        // Свойства (хуёйства...)
        public string FirstName
        {
            get { return firstName; }
            set
            {
                if (value.Length > 32)
                {
                    throw new ArgumentException("Строка содержит больше 32 символа.");
                }
                else
                {
                    firstName = value.ToLower().ToUpper(0);
                }
            }
        }
        public string LastName
        {
            get { return lastName; }
            set
            {
                if (value.Length > 32)
                {
                    throw new ArgumentException("Строка содержит больше 32 символа.");
                }
                else
                {
                    lastName = value.ToLower().ToUpper(0);
                }
            }
        }
        public char Grade
        {
            get { return grade; }
            set
            {
                grade = value.ToString().ToUpper().ElementAt(0);
            }
        }
        public DateTime Birthday
        {
            get { return birthday; }
            set
            {
                if (value > Constants.MinBirthday && value < Constants.MaxBirthday)
                {
                    birthday = value;
                }
                else
                {
                    throw new ArgumentException("Дата рождения выходит из диапазона, НАХУЙ.");
                }
            }
        }
        public string City
        {
            get { return city; }
            set
            {
                if (value.Length > 32)
                {
                    throw new ArgumentException("Строка содержит больше 32 символа.");
                }
                else
                {
                    city = value;
                }
            }
        }
        public string PhoneNumber
        {
            get { return phoneNumber; }
            set
            {
                // ToDo: проверОЧКА на "являются ли все символы цифрами?"
                if (phoneNumber[0] != '+' || phoneNumber.Length != 14)
                {
                    throw new ArgumentException("не равянется плюсу, говёно.");
                }
                else
                {
                    phoneNumber = value;
                }
            }
        }

        // Поля (бля...)
        private string firstName;
        private string lastName;
        private char grade;
        private DateTime birthday;
        private string city;
        private string phoneNumber;

        // Конструктор (хуюктор...)
        public Student(string firstName, string lastName, char grade, DateTime birthday)
        {
            FirstName = firstName;
            LastName = lastName;
            Grade = grade;
            Birthday = birthday;
        }
    }
}
