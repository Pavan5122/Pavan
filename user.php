// User model (models/User.php)
namespace app\models;

use yii\db\ActiveRecord;

class User extends ActiveRecord
{
    public static function tableName()
    {
        return 'user'; // Assuming 'user' is the name of your database table for users
    }

    public function rules()
    {
        return [
            [['username', 'email', 'password'], 'required'],
            [['email'], 'email'],
            [['username', 'email'], 'unique'],
            [['password'], 'string', 'min' => 6],
        ];
    }

    public function attributeLabels()
    {
        return [
            'username' => 'Username',
            'email' => 'Email',
            'password' => 'Password',
        ];
    }

    // You can define other behaviors here, such as beforeSave, afterSave, etc.
}
