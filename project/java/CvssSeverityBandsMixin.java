package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssSeverityBandsMixin  {

  private float baseScore;
  private String baseSeverity;


}