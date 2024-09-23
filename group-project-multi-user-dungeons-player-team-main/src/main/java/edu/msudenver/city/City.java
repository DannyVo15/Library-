package edu.msudenver.city;

import com.fasterxml.jackson.annotation.JsonProperty;
import edu.msudenver.country.Country;

import javax.persistence.*;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "cities")
@IdClass(CityId.class)
public class City {
    @Id
    @Column(name = "postal_code")
    private String postalCode;

    @Id
    @Column(name = "country_code")
    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
    private String countryCode;

    @ManyToOne()
    @JoinColumn(name = "country_code", referencedColumnName = "country_code", insertable = false, updatable = false)
    @JsonProperty(access = JsonProperty.Access.READ_ONLY)
    private Country country;

    @Column(name = "name")
    @NotNull(message = "City name cannot be null")
    private String name;

    public City(String postalCode, Country country, String countryCode, String name) {
        this.postalCode = postalCode;
        this.country = country;
        this.countryCode = countryCode;
        this.name = name;
    }

    public City() {
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public Country getCountry() {
        return country;
    }

    public void setCountry(Country country) {
        this.country = country;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
