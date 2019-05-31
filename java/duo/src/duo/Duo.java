/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package duo;

import java.sql.Connection;
import java.sql.DriverManager;
import javax.swing.JOptionPane;

/**
 *
 * @author user
 */
public class Duo {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        Connection conn = connDuo();
    }
    
    
    public static Connection connDuo(){
        Connection conn = null;
        try{
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            conn = DriverManager.getConnection("jdbc:sqlserver://localhost;databaseName=duo", "sa", "123");
            JOptionPane.showMessageDialog(null, "Подключено");
            return conn;
        } catch (Exception e){
            JOptionPane.showMessageDialog(null, e.getMessage());
            return null;
        }
    }
    
}
