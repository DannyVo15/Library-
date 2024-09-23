package edu.msudenver.country;


import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "countries")
public class Country {
    @Column(name = "country_name")
    @NotNull(message = "countryName cannot be null")
    private String countryName;
    @Id
    @Column(name = "country_code")
    private String countryCode;

    public Country(String countryName, String countryCode) {
        this.countryName = countryName;
        this.countryCode = countryCode;
    }

    public Country(String countryCode) {
        this.countryCode = countryCode;
    }

    public Country() {
    }

    public String getCountryName() {
        return countryName;
    }

    public Country setCountryName(String countryName) {
        this.countryName = countryName;
        return this;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public Country setCountryCode(String countryCode) {
        this.countryCode = countryCode;
        return this;
    }
}
